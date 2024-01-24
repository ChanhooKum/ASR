import torch
import time

def benchmark_gpu(gpu_id, matrix_size):
    # Set the device to the specified GPU
    device = torch.device(f'cuda:{gpu_id}' if torch.cuda.is_available() else 'cpu')
    print(f"Running on: {device}")

    # Create random matrices
    matrix1 = torch.rand(matrix_size, matrix_size, device=device)
    matrix2 = torch.rand(matrix_size, matrix_size, device=device)

    # Warm-up run (to handle initialisation overhead)
    for _ in range(10):
        _ = torch.matmul(matrix1, matrix2)

    # Synchronize to ensure accurate timing
    torch.cuda.synchronize(device)

    # Benchmark
    start_time = time.time()
    for _ in range(100):
        _ = torch.matmul(matrix1, matrix2)
    torch.cuda.synchronize(device)
    end_time = time.time()

    print(f"Time taken for matrix size {matrix_size}: {end_time - start_time} seconds")

# Example Usage
gpu_id = 1  # Change based on your GPU ID
matrix_size = 4096  # You can adjust this based on your GPU's capability

benchmark_gpu(gpu_id, matrix_size)
