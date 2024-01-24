import torch
import torch.nn as nn
import time
import os  # Import the os module

def benchmark_specific_gpus(matrix_size, gpu_ids):
    # Check if CUDA is available and determine the number of GPUs
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"Running on {num_gpus} GPUs")

        # Check if the specified GPUs are valid
        if max(gpu_ids) >= num_gpus:
            print("Invalid GPU IDs specified.")
            return

        # Set CUDA_VISIBLE_DEVICES to specify the GPUs to use
        torch.cuda.set_device(gpu_ids[0])  # Set the first specified GPU as the main device
        os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, gpu_ids))

        # Create random matrices on the specified GPUs
        matrices = [torch.rand(matrix_size, matrix_size).cuda() for _ in gpu_ids]

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

        print(f"Time taken for matrix size {matrix_size} on GPUs {gpu_ids}: {end_time - start_time} seconds")
    else:
        print("CUDA is not available.")

# Example Usage
matrix_size = 4096  # You can adjust this based on your GPU's capability
#gpu_ids = [0, 1, 2, 3]  # Specify the GPU IDs you want to use
gpu_ids = [1, 2]  # Specify the GPU IDs you want to use
benchmark_specific_gpus(matrix_size, gpu_ids)
