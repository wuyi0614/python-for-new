# Tutorial collection: the python-for-new repository

## What You Will Gain from This Tutorial?

- Problem-solving skills using Python for projects

- Mastery of essential Python concepts

- Understanding of classical theories and algorithms

## Who Is This Tutorial For?

- Beginners seeking systematic Python learning from scratch

- Learners needing quick Python proficiency for immediate tasks

- Individuals interested in exploring Python fundamentals

## Quick config

**1. Execute the following codes to install your own Python interpreter development environment (IDE)**

> Use your Terminal.app to download the latest Miniconda3 image from Tsinghua Mirror. 
> Find the correct image for your OS from the following urls:
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-Linux-aarch64.sh
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-Linux-s390x.sh
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-Linux-x86_64.sh
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-MacOSX-arm64.sh [Apple Silicon]
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-MacOSX-x86_64.sh [Intel Chip]
> - https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-Windows-x86_64.exe

### 1.1 MacOS (or Linux)

You may find it hard to download `conda` images from its [official site](https://docs.anaconda.net.cn/miniconda/install/), 
so it's better to try home mirrors, such as Tsinghua's open source mirrors: 

```bash
# ... run the following bash codes in your terminal
curl https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py312_25.1.1-2-MacOSX-x86_64.sh -o ./miniconda.sh
bash ./miniconda.sh
rm ./miniconda.sh
```

### 1.2 Windows (X64 arch)

Open your browser and put this url: `https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/` into your browser and open it. 
Press `Ctrl + F` and search `Miniconda3-py312_25.1.1-2-Windows-x86_64.exe`, and then click & download. 

**2. Download professional IDE and get used to it soon**

Visit jetbrains's official site to obtain the installer, for example:
- MacOS: https://www.jetbrains.com/zh-cn/pycharm/download/?section=mac 
- Win: https://www.jetbrains.com/zh-cn/pycharm/download/?section=windows

You can also obtain a valid educational license for your Pycharm IDE: https://www.jetbrains.com/zh-cn/community/education/#students/. 

**3. Use `pipenv` to manage your Python dependencies**

View `pipenv` [documentation](https://pipenv.pypa.io/en/latest/) to know advanced `pipenv` usage for future learning & working.
(Ensure the `pip` and `conda` environments ready for utilisation)

```bash
# run `pipenv install` to initiate the config file
pipenv install
# ... then you can manually configure your interpreter in your Pycharm IDE
```

## Contact

You may be interested in further studies or practices, please contact me by:

> @Maintainer, email: `wymario@163.com`
