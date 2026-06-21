import argparse
import shutil
import subprocess
from pathlib import Path


def run(command, cwd):
    print(f"> {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def remove_directory(path):
    if path.exists():
        print(f"Removing {path}")
        shutil.rmtree(path)


def main():
    parser = argparse.ArgumentParser(description="Build, test, and package the C++ demo SDK.")
    parser.add_argument(
        "--configuration",
        default="Release",
        choices=["Debug", "Release"],
        help="Build configuration.",
    )
    parser.add_argument(
        "--generator",
        default="Ninja",
        help="CMake generator to use on the Windows build VM.",
    )
    parser.add_argument(
        "--c-compiler",
        default="clang",
        help="C compiler executable used by CMake.",
    )
    parser.add_argument(
        "--cxx-compiler",
        default="clang++",
        help="C++ compiler executable used by CMake.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    build_dir = repo_root / "build"
    artifacts_dir = repo_root / "artifacts"

    print(f"Repo root: {repo_root}")
    print(f"Configuration: {args.configuration}")
    print(f"CMake generator: {args.generator}")
    print(f"C compiler: {args.c_compiler}")
    print(f"C++ compiler: {args.cxx_compiler}")

    remove_directory(build_dir)
    remove_directory(artifacts_dir)

    configure_command = [
        "cmake",
        "-S",
        str(repo_root),
        "-B",
        str(build_dir),
        "-G",
        args.generator,
        f"-DCMAKE_C_COMPILER={args.c_compiler}",
        f"-DCMAKE_CXX_COMPILER={args.cxx_compiler}",
    ]

    run(configure_command, cwd=repo_root)

    run(
        [
            "cmake",
            "--build",
            str(build_dir),
            "--config",
            args.configuration,
            "--parallel",
        ],
        cwd=repo_root,
    )

    run(
        [
            "ctest",
            "--test-dir",
            str(build_dir),
            "-C",
            args.configuration,
            "--output-on-failure",
        ],
        cwd=repo_root,
    )

    run(
        [
            "cmake",
            "--install",
            str(build_dir),
            "--config",
            args.configuration,
            "--prefix",
            str(artifacts_dir),
        ],
        cwd=repo_root,
    )

    print(f"Package output created at: {artifacts_dir}")


if __name__ == "__main__":
    main()
