#!/bin/bash

echo "=============================================="
echo "   REPLICATION PIPELINE — Many Analysts Style"
echo "=============================================="
echo

# Docker image name
IMAGE="rep-study"

# Check that the docker image exists
if ! docker image inspect $IMAGE >/dev/null 2>&1; then
    echo "[ERROR] Docker image '$IMAGE' not found."
    echo "Run: docker build -t rep-study -f replicability/Dockerfile ."
    exit 1
fi

# Output directory for logs
OUTDIR="scripts/results"
mkdir -p "$OUTDIR"

run_variant () {
    ID=$1
    OUTCOME=$2
    SKIN=$3
    COV=$4
    MISSING=$5

    echo
    echo "--------------------------------------------------"
    echo " Running Variant $ID"
    echo " Outcome:   $OUTCOME"
    echo " Skin:      $SKIN"
    echo " Covariates:$COV"
    echo " Missing:   $MISSING"
    echo "--------------------------------------------------"

    LOGFILE="$OUTDIR/variant_${ID}.log"

    docker run --rm rep-study \
        --outcome $OUTCOME \
        --skin $SKIN \
        --cov $COV \
        --missing $MISSING \
        > "$LOGFILE" 2>&1

    echo "→ Results saved to: $LOGFILE"
}

# ================================
# RUN ALL 8 VARIANTS FROM TABLE
# ================================

run_variant 1 "logit"   "continuous" "performance" "dropna"
run_variant 2 "logit"   "binary"     "performance" "dropna"
run_variant 3 "poisson" "continuous" "full"        "dropna"
run_variant 4 "logit"   "continuous" "none"        "dropna"
run_variant 5 "logit"   "binary"     "full"        "mean"
run_variant 6 "poisson" "binary"     "performance" "dropna"
run_variant 7 "logit"   "continuous" "full"        "mean"
run_variant 8 "poisson" "continuous" "none"        "dropna"

echo
echo "=============================================="
echo "         ALL VARIANTS COMPLETED"
echo " Logs stored in scripts/results/"
echo "=============================================="
