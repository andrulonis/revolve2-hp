So a very brief explanation:

Installation guide in HP drive>documentation>installation doc karine:
https://drive.google.com/drive/folders/1m9UoMw5NXw_ffm4H3-VKz1efJiWw-3zn?usp=sharing

Set configuration of experiment in by changing the default parameter values: <revolve>/core/revolve2/config.py

Make directory "honours2021" in home. set chmod to 775. Make yourself owner with chown. Use:
```
sudo mkdir /home/honours2021 
sudo chmod 775 /home/honours2021
sudo chown <your user> /home/honours2021
``` 

From revolve's root, run the experiment with:
./experiments/default_study/run-experiment.sh

Then run analysis from root with:
./experiments/default_study/run-analysis.sh

Results in /home/honours2021

The video function works now too: ./experiments/default_study/makevideos.sh
    Do note that it only works with 1 monitor. 