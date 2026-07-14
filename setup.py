from setuptools import setup, find_packages

setup(
    name="play-integrity-helper",
    version="0.1.0",
    description="One-click Play Integrity helper for cloud phones",
    author="qtphone.com",
    author_email="contact@qtphone.com",
    url="https://github.com/luoshixin93-sudo/play-integrity-helper",
    packages=find_packages(),
    install_requires=[
        "adb-shell>=0.4.4",
        "click>=8.0.0",
        "rich>=13.0.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "pih=play_integrity_helper.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Build Tools",
    ],
)
