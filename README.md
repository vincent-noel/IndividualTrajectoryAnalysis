## Use with binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vincent-noel/IndividualTrajectoryAnalysis/main?filepath=ObservedSTG.ipynb)

## Use with docker
To run this notebook using the built docker image, run : 
```
docker run -p 8888:8888 -d sysbiocurie/indtraj
```

Then open a browser at the following url : <a href="http://localhost:8888/tree/IndividualTrajectoryAnalysis">http://localhost:8888/tree/IndividualTrajectoryAnalysis/</a>


## Use with conda
Clone this github repository : 
```
git clone https://github.com/vincent-noel/IndividualTrajectoryAnalysis.git
```

Build the conda environment : 
```
conda create -n indtraj -c colomoto pymaboss networkx pandas notebook
```

Activate it : 
```
conda activate indtraj
```

Run the notebook: 
```
jupyter notebook
```
 
Then open a browser at the following url : <a href="http://localhost:8888/tree/IndividualTrajectoryAnalysis/">http://localhost:8888/tree/IndividualTrajectoryAnalysis/</a>
