

# MPI Matrix Multiplication

This program performs matrix multiplication in parallel using MPI. It splits the computation across multiple processes and gathers the results at the root process.

## Requirements

To run this program, you need:
- An MPI implementation (e.g., OpenMPI)
- A C++ compiler with MPI support (e.g., `mpicc` from OpenMPI)

### Installation

You can install OpenMPI and required dependencies with the following command:

```bash
sudo apt-get update
sudo apt-get install -y openmpi-bin openmpi-common libopenmpi-dev
```

Ensure that MPI is installed correctly by running:

```bash
mpirun --version
```

## Compilation

To compile the program, use `mpicc` (MPI C++ compiler). In a terminal, run:

```bash
mpicc -o matrix_multiply exercise22.cpp
```

This will generate an executable file named `matrix_multiply`.

## Running the Program

To run the program with MPI, you can use `mpirun`. The following example runs the program using 4 processes:

```bash
mpirun --allow-run-as-root --oversubscribe -np 4 ./matrix_multiply
```

### Options:

- `--allow-run-as-root`: Allows running as the root user (since this may be required in some environments, but it's generally discouraged).
- `--oversubscribe`: Forces MPI to run more processes than available CPU cores, which can be useful in testing.
- `-np 4`: Specifies the number of processes to use (in this case, 4).

## Example Input

The program initializes two matrices `A` and `B` and multiplies them to get the result `C`. The matrices are initialized within the code with hardcoded or randomly generated values.

## Output

The result matrix `C` will be printed to the console after the computation, along with the time taken to perform the matrix multiplication.
