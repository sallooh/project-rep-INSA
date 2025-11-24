#!/bin/bash

echo "=============================================="
echo "            REPRODUCIBILITY TEAM27            "
echo "=============================================="
echo

# Docker image name
IMAGE="reproductibility-project"
DOCKERFILE="teams/team27/Dockerfile"

# Check that the docker image exists; if not, build it
if ! sudo docker image inspect $IMAGE >/dev/null 2>&1; then
    echo "[INFO] Docker image '$IMAGE' not found."
    echo "[INFO] Building Docker image using $DOCKERFILE ..."
    sudo docker build -t $IMAGE -f $DOCKERFILE .
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] Docker image build failed."
        exit 1
    fi

    echo "[INFO] Docker image '$IMAGE' successfully built."
fi

# Output directory for logs
OUTDIR="scripts/results"
mkdir -p "$OUTDIR"

LOGFILE="$OUTDIR/reproducibility_result.log"

sudo docker run --rm $IMAGE \
    > "$LOGFILE" 2>&1

echo "→ Results saved to: $LOGFILE"
