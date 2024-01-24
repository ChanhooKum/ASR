import torch
import torch.nn as nn
import time

def benchmark_multi_gpu(matrix_size):
    # Check if CUDA is available and determine the number of GPUs
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"Running on {num_gpus} GPUs")

        # Create random matrices
        matrices = []
        for _ in range(num_gpus):
            matrix = torch.rand(matrix_size, matrix_size).cuda()
            matrices.append(matrix)

        # Warm-up run (to handle initialization overhead)
        for _ in range(10):
            results = [matrix @ matrix for matrix in matrices]

        # Synchronize to ensure accurate timing
        torch.cuda.synchronize()

        # Benchmark
        start_time = time.time()
        for _ in range(100):
            results = [matrix @ matrix for matrix in matrices]
        torch.cuda.synchronize()
        end_time = time.time()

        print(f"Time taken for matrix size {matrix_size} on {num_gpus} GPUs: {end_time - start_time} seconds")
    else:
        print("CUDA is not available.")

# Example Usage
matrix_size = 4096  # You can adjust this based on your GPU's capability
benchmark_multi_gpu(matrix_size)
