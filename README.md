# C++ Jenkins Demo

This project demonstrates a small Windows C++ SDK build using this flow:

```text
Bitbucket repo -> Jenkins pipeline -> Windows VM agent -> Python build script -> CMake -> Ninja -> C++ compiler
```

## Build Machine Tools

The Windows VM build machine is non-interactive and does not need the Visual Studio IDE.

Install these CLI tools on the Windows VM:

- Git
- Python
- CMake
- Ninja
- Java JDK for the Jenkins agent
- A C++ compiler/toolchain

Recommended compiler options:

- Visual Studio Build Tools only, without the Visual Studio IDE, for MSVC-compatible Windows SDK builds
- LLVM/Clang for a CLI-first toolchain
- MinGW-w64 GCC if the project is designed for the MinGW ecosystem

For many commercial Windows SDKs, the usual setup is:

```text
Visual Studio Build Tools + CMake + Ninja
```

That means the Visual Studio IDE is not installed, but the command-line compiler, linker, libraries, and Windows SDK are installed.

## Local Build Command

From the repo root:

```powershell
python scripts\build.py --configuration Release
```

The final package output is written to:

```text
artifacts
```
