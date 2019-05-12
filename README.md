# AI-Competition-Connect4
Starter files for the First School of AI Competition. The objective is to create an agent capable of playing Connect4

### Rules
1. Your agent must return a valid move within the time limit of 0.25 seconds. Failure to do so will result in losing the match.
2. Your agent must be able to run on [This Machine](https://laptopmedia.com/laptop-specs/rog-gl553vd/).
3. Only the Libraries in the requirements.txt file will be available on the competition environment.


### Getting Started
1. Make sure you have [Python 3.6](https://www.python.org/) installed.

2. Clone the repository
    ```bash
    git clone https://github.com/SchoolofAI-Vancouver/AI-Competition-Connect4.git
    ```
    
3. Use [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to create a new environment and install dependencies. <br>[Click Here](https://nbviewer.jupyter.org/github/johannesgiorgis/school_of_ai_vancouver/blob/master/intro_to_data_science_tools/01_introduction_to_conda_and_jupyter_notebooks.ipynb) if you need a detail guide on using conda.

    - __Linux__ or __Mac__: 
    ```bash
    conda create --name tournament python=3.6
    source activate tournament
    conda install numpy
    conda install matplotlib
    conda install jupyter notebook
    ```
  
    - __Windows__: 
    ```bash
    conda create --name tournament python=3.6 
    activate tournament
    conda install numpy
    conda install matplotlib
    conda install jupyter notebook
    ```

### Instructions
Navigate to the directory and open Connect4.ipynb

    jupyter notebook Connect4.ipynb
