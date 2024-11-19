# R.I.C.E. Fields
A collection of **R**ace **I**nspired **C**osmetic **E**nhancements.

## Introduction

This repository hosts various Themes, Icons, and Configs used for modifying the appearance of a Linux environment.

## Organizational Structure

Since different desktop environments have different ways of handling themes, icons, and configs, this repository follows this structure:

```
rice/
├── icons/
│   └── <desktop_environment>/
│       └── <linux_distribution>/
├── themes/
│   └── <desktop_environment>/
│       └── <linux_distribution>/
└── configs/
    └── <desktop_environment>/
        └── <linux_distribution>/
```

## Development Process

### Testing and Implementation Flow

As development continues and knowledge of Linux customization grows, new themes, icons, and configs will be added following this process:

1. Test a theme/icon/config on a specific distribution + environment
2. Add it to the repository in the appropriate location
3. Mark it as tested on that distribution + environment
4. Test compatibility with other distributions + environments
5. Update testing status accordingly
6. Repeat process for new additions

### Implementation Status

#### Desktop Environments
- [ ] GNOME
- [ ] KDE_PLASMA
- [ ] XFCE
- [x] CINNAMON
- [ ] MATE
- [ ] LXQT
- [ ] BUDGIE
- [ ] LXDE
- [ ] DDE
- [ ] PANTHEON

#### Linux Distributions
- [x] MINT
- [ ] UBUNTU
- [ ] DEBIAN
- [ ] MANJARO
- [ ] ARCH
- [ ] FEDORA

#### Currently Using
----------------------------------------------
| Environment |   e   |   d   | Distribution |
| :---------: | :---: | :---: | :----------: |
|    GNOME    |   -   |   x   |     MINT     |
| KDE_PLASMA  |   -   |   -   |    UBUNTU    |
|    XFCE     |   -   |   -   |    DEBIAN    |
|  CINNAMON   |   x   |   -   |   MANJARO    |
|    MATE     |   -   |   -   |     ARCH     |
|    LXQT     |   -   |   -   |    FEDORA    |
|   BUDGIE    |   -   |   -   |      -       |
|    LXDE     |   -   |   -   |      -       |
|     DDE     |   -   |   -   |      -       |
|  PANTHEON   |   -   |   -   |      -       |
----------------------------------------------
## Future Plans

### Short-term Goals
- Test additional distributions to identify preferred distro & environment
- Create database to track theme/icon/config compatibility across distributions and environments

### Notes on Compatibility
Since compatibility across distribution + environment combinations cannot be predicted with certainty, all components will be thoroughly tested and documented before being marked as compatible.
