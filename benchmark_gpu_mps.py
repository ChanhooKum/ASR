import torch
import time

def benchmark_mps(matrix_size):
    # Check if MPS is available
    if not torch.backends.mps.is_available():
        print("MPS device not found.")
        return

    # Set the device to MPS
    device = torch.device("mps")
    print(f"Running on: {device}")

    # Create random matrices
    matrix1 = torch.rand(matrix_size, matrix_size, device=device)
    matrix2 = torch.rand(matrix_size, matrix_size, device=device)

    # Warm-up run
    for _ in range(10):
        _ = torch.matmul(matrix1, matrix2)

    # Synchronize to ensure accurate timing
    # Note: MPS might not require explicit synchronization like CUDA
    # torch.cuda.synchronize() equivalent for MPS might not be necessary

    # Benchmark
    start_time = time.time()
    for _ in range(100):
        _ = torch.matmul(matrix1, matrix2)
    # Synchronize if necessary for MPS
    end_time = time.time()

    print(f"Time taken for matrix size {matrix_size}: {end_time - start_time} seconds")

# Example Usage
matrix_size = 8192  # Adjust based on your device's capability
benchmark_mps(matrix_size)
