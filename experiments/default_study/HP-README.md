So a very brief explanation:

Installation guide in HP drive>documentation>installation doc karine:
https://drive.google.com/drive/folders/1m9UoMw5NXw_ffm4H3-VKz1efJiWw-3zn?usp=sharing

Set configuration of experiment in by changing the default parameter values: <revolve>/core/revolve2/config.py
!NOTE after every single change to config.py, run ./dev-requirements.sh


Change terrain at /home/honours2021/revolve2-hp/runners/isaacgym/revolve2/runners/isaacgym/_local_runner.py

There is a folder "other_terrains" with all of your terrains (except Sohaib's, cuz it will be uploaded in 20 business days).

Make directory "honours2021" in home or in storage, this will be the output location. The ripper already has this output folder. set chmod to 777. Make yourself owner with chown. Use:
```
sudo mkdir /home/honours2021 
sudo chmod 777 /home/honours2021
sudo chown <your user> /home/honours2021
``` 

From revolve's root, run the experiment with:
./experiments/default_study/run-experiment.sh

Then run analysis from root with:
./experiments/default_study/run-analysis.sh

Results in /home/honours2021

The video function works now too: ./experiments/default_study/makevideos.sh
    Do note that it only works with 1 monitor. 