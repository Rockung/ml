FACENET_BASE=~dapeng/dev/facenet

# export PYTHONPAHT="$FACENET_BASE/src"

for N in {1..4}; do \
    python src/align/align_dataset_mtcnn.py \
        $FACENET_BASE/datasets/lfw/raw \
        $FACENET_BASE/datasets/lfw/lfw_mtcnnpy_160 \
        --image_size 160 --margin 32 --random_order \
        --gpu_memory_fraction 0.25 & done

