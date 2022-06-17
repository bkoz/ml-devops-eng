# Scalable Pipelines MLOps Course
## Notes

### Aequitas

Exercise: Using Aequitas to find bias in the [car evaluation dataset](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)

### Data Version Control (DVC)

```
pip install dvc 'dvc[gdrive]'
```

Create a datafile `id.csv` and use dvc.
```
git init
dvc init
mkdir ../local_remote
dvc remote add -d localremote ../local_remote

dvc add id.csv
git add .gitignore id.csv.dvc
git commit -m "Initial commit of tracked sample.csv"
dvc push
```

#### Remote Storage
```
dvc remote add <remote-name> <remote-url>
dvc remote add gdrive gdrive://<unique-id-from-sharing-link>
dvc push -r gdrive
```

#### DVC Pipelines

The parameters we define get stored in `param.yaml` and the specification of the pipeline is stored in `dvc.yaml` both of which can be version controlled using Git thus enabling reproducibility of current and past results.

Create a pipeline with 2 stages. The dependencies (input) and outs (output)
determine how the stages are connected.

```
dvc run -n prepare -d prepare.py -d fake_data.csv -o X.csv -o y.csv python prepare.py

dvc run -n train -d prepare.py -d X.csv -d y.csv -p train.test_size,train.random_state -o model.pkl python train.py
```

Run the entire pipeline.
```
dvc repro
```

Print the DAG.
```
dvc dag
```
```
+---------+  
| prepare |  
+---------+  
      *      
      *      
      *      
 +-------+   
 | train |   
 +-------+ 
 ```

### References

[IBM ML Bias Paper](https://developer.ibm.com/articles/machine-learning-and-bias/?mhsrc=ibmsearch_a&mhq=machine%20learning%20and%20bias)

[Aequiatas examples](https://github.com/dssg/aequitas/blob/master/docs/source/examples/compas_demo.ipynb)
