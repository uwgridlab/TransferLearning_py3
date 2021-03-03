# TransferLearning_py3
TL re-implemented in Python 3

User chooses day 1/2, picture set 1/2, and pictures per group of 3/4/5
Day 1: 200 trials of groups 1 and 2 from chosen set
Day 2: 50 trials of groups 1 and 2 from chosen set + 200 trials of groups 3 and 4 from chosen set

Trials consist of .5s fixation cross, 1.5s image presentation, 1s feedback ("correct" or "incorrect"), and 1s inter-trial interval.

Output CSV files contain some duplicate info to try to keep consistent column name info across versions. The following columns will match up exactly to the data that was saved in column of the same name in the previous version:
trials.thisNN
stim_image
left_image
right_image
choice
ans_correctness
group_pair
key_resp_2.rt
Note that there are slight differences in key_resp_2.keys and other trial indexing columns in the two versions. The data in ans_correctness is identical to the data in key_resp_2.corr.

Additional columns save user choices:
day
picture_set
num_per_group