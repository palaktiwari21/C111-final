import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go
df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()
#fig=ff.create_distplot([data],['Math_score'],show_hist=False)
#fig.show()
population_mean=statistics.mean(data)
population_std_deviation=statistics.stdev(data)
print( "Population mean is : ",population_mean)
print( "Population standard deviation is : ",population_std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
mean=statistics.mean(mean_list)
print('Mean of Sampling Distribution : ',mean)
#fig=ff.create_distplot([mean_list],['studentMarks'],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name='Mean'))
#fig.show()
std_deviation=statistics.stdev(mean_list)
print('Standard Deviation of Sampling Distribution : ',std_deviation)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print('std1',first_std_deviation_start,first_std_deviation_end)
print('std2',second_std_deviation_start,second_std_deviation_end)
print('std3',third_std_deviation_start,third_std_deviation_end)
fig=ff.create_distplot([mean_list],['student marks'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
#fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='FIRST STANDARD DEVIATION START'))
#fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='FIRST STANDARD DEVIATION END'))
#fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='SECOND STANDARD DEVIATION START'))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='SECOND STANDARD DEVIATION END'))
#fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='THIRD STANDARD DEVIATION START'))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='THIRD STANDARD DEVIATION END'))
#fig.show()

df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()
mean_of_sample3=statistics.mean(data)
print('Mean of Sample 3 is : ',mean_of_sample3)
fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode='lines',name='MEAN OF SAMPLE3'))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='FIRST STANDARD DEVIATION END'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='SECOND STANDARD DEVIATION END'))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='THIRD STANDARD DEVIATION END'))
fig.show()

