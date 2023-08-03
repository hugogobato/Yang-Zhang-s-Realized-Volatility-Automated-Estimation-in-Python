"""

@authors: Hugo Gobato Souto* and Amir Moradi**

*International School of Business at HAN University of Applied Sciences, Ruitenberglaan 31, 
6826 CC Arnhem, the Netherlands; H.GobatoSouto@han.nl; https://orcid.org/0000-0002-7039-0572
Contact author.

**International School of Business at HAN University of Applied Sciences, Ruitenberglaan 31, 
6826 CC Arnhem, the Netherlands; amir.moradi@han.nl; https://orcid.org/0000-0003-1169-7192. 
"""


# Software

def Yang_Zhang_RV_yahoo(tickers, start=None, end=None, period=None, interval=None):
    # importing needed libraries
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    
    #Data extraction
    if period==None:
        data=yf.download(tickers=tickers, start=start, end=end, interval=interval)
    else:
        data=yf.download(tickers=tickers, period=period, interval=interval)
    #dropping N/A values
    if data.isnull().values.any()==True:
        data=data.dropna()
        print("Rows with missing values were removed")
    else:
        data=data
        
    # Yang_Zhang_RV formula is give as:
    # RV^2 = Vo + k*Vc + (1-k)*Vrs
    # where Vo = 1/(n-1)*sum(Oi-Obar)^2
    # with oi = normalized opening price at time t and Obar = mean of normalized opening prices
    # Vc = = 1/(n-1)*sum(ci-Cbar)^2
    # with ci = normalized close price at time t and Cbar = mean of normalized close prices
    # k = 0.34/(1.34+(n+1)/(n-1))
    # with n = total number of days or time periods considered
    # Vrs (Rogers & Satchell RV proxy) = ui(ui-ci)+di(di-ci)
    # with ui = ln(Hi/Oi), ci = ln(Ci/Oi), di=(Li/Oi), oi = ln(Oi/Ci-1)
    # where Hi = high price at time t and Li = low price at time t
    
    data["ui"]=np.log(np.divide(data["High"][1:],data["Open"][1:]))
    data["ci"]=np.log(np.divide(data["Close"][1:],data["Open"][1:]))
    data["di"]=np.log(np.divide(data["Low"][1:],data["Open"][1:]))
    data["oi"]=np.log(np.divide(data["Open"][1:],data["Close"][:len(data)-1]))
    data=data[1:]
    data["RS"]=data["ui"]*(data["ui"]-data["ci"])+data["di"]*(data["di"]-data["ci"])
    RS_var= data["RS"].groupby(pd.Grouper(freq='1D')).mean().dropna()
    Vc_and_Vo=data[["oi", "ci"]].groupby(pd.Grouper(freq='1D')).var().dropna()
    n=int(len(data)/len(RS_var))
    k = 0.34/(1.34+(n+1)/(n-1))
    Yang_Zhang_RV=np.sqrt((1-k)*RS_var+Vc_and_Vo["oi"]+Vc_and_Vo["ci"]*k)
    Yang_Zhang_RV_df=pd.DataFrame(Yang_Zhang_RV)
    Yang_Zhang_RV_df.rename(columns={0: "Yang & Zhang RV proxy"},inplace=True)
    
    return Yang_Zhang_RV_df

def Yang_Zhang_RV_own_data(data):
    # importing needed libraries
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    
    # Yang_Zhang_RV formula is give as:
    # RV^2 = Vo + k*Vc + (1-k)*Vrs
    # where Vo = 1/(n-1)*sum(Oi-Obar)^2
    # with oi = normalized opening price at time t and Obar = mean of normalized opening prices
    # Vc = = 1/(n-1)*sum(ci-Cbar)^2
    # with ci = normalized close price at time t and Cbar = mean of normalized close prices
    # k = 0.34/(1.34+(n+1)/(n-1))
    # with n = total number of days or time periods considered
    # Vrs (Rogers & Satchell RV proxy) = ui(ui-ci)+di(di-ci)
    # with ui = ln(Hi/Oi), ci = ln(Ci/Oi), di=(Li/Oi), oi = ln(Oi/Ci-1)
    # where Hi = high price at time t and Li = low price at time t
    
    data["ui"]=np.log(np.divide(data["High"][1:],data["Open"][1:]))
    data["ci"]=np.log(np.divide(data["Close"][1:],data["Open"][1:]))
    data["di"]=np.log(np.divide(data["Low"][1:],data["Open"][1:]))
    data["oi"]=np.log(np.divide(data["Open"][1:],data["Close"][:len(data)-1]))
    data=data[1:]
    data["RS"]=data["ui"]*(data["ui"]-data["ci"])+data["di"]*(data["di"]-data["ci"])
    RS_var= data["RS"].groupby(pd.Grouper(freq='1D')).mean().dropna()
    Vc_and_Vo=data[["oi", "ci"]].groupby(pd.Grouper(freq='1D')).var().dropna()
    n=int(len(data)/len(RS_var))
    k = 0.34/(1.34+(n+1)/(n-1))
    Yang_Zhang_RV=np.sqrt((1-k)*RS_var+Vc_and_Vo["oi"]+Vc_and_Vo["ci"]*k)
    Yang_Zhang_RV_df=pd.DataFrame(Yang_Zhang_RV)
    Yang_Zhang_RV_df.rename(columns={0: "Yang & Zhang RV proxy"},inplace=True)
    
    return Yang_Zhang_RV_df
    
    
    
def Multivariate_Yang_Zhang_RV_own_data(data_list):
    Multivariate_Yang_Zhang_RV=[]
    for i in range(len(data_list)):
        Yang_Zhang_RV_df=Yang_Zhang_RV_own_data(data=data_list[i])
        Multivariate_Yang_Zhang_RV.append(Yang_Zhang_RV_df)
    return Multivariate_Yang_Zhang_RV
    
    
def Multivariate_Yang_Zhang_RV_yahoo(tickers, start=None, end=None, period=None, interval=None):
    # importing needed libraries
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    
    #Data extraction
    if period==None:
        data=yf.download(tickers=tickers, start=start, end=end, interval=interval)
    else:
        data=yf.download(tickers=tickers, period=period, interval=interval)
    #dropping N/A values
    if data.isnull().values.any()==True:
        data=data.dropna()
        print("Rows with missing values were removed")
    else:
        data=data

    data=data.unstack().reset_index(name="Actuals").rename(columns={"level_1":"Stocks"}).set_index("Datetime").pivot(columns=['Stocks','level_0'])
    data=data['Actuals']
        
    # Yang_Zhang_RV formula is give as:
    # RV^2 = Vo + k*Vc + (1-k)*Vrs
    # where Vo = 1/(n-1)*sum(Oi-Obar)^2
    # with oi = normalized opening price at time t and Obar = mean of normalized opening prices
    # Vc = = 1/(n-1)*sum(ci-Cbar)^2
    # with ci = normalized close price at time t and Cbar = mean of normalized close prices
    # k = 0.34/(1.34+(n+1)/(n-1))
    # with n = total number of days or time periods considered
    # Vrs (Rogers & Satchell RV proxy) = ui(ui-ci)+di(di-ci)
    # with ui = ln(Hi/Oi), ci = ln(Ci/Oi), di=(Li/Oi), oi = ln(Oi/Ci-1)
    # where Hi = high price at time t and Li = low price at time t
    
    Multivariate_Yang_Zhang_RV=[]
    for i in range(len(tickers)):
        data1=data[tickers[i]]
        data1["ui"]=np.log(np.divide(data1["High"][1:],data1["Open"][1:]))
        data1["ci"]=np.log(np.divide(data1["Close"][1:],data1["Open"][1:]))
        data1["di"]=np.log(np.divide(data1["Low"][1:],data1["Open"][1:]))
        data1["oi"]=np.log(np.divide(data1["Open"][1:],data1["Close"][:len(data1)-1]))
        data1=data1[1:]
        data1["RS"]=data1["ui"]*(data1["ui"]-data1["ci"])+data1["di"]*(data1["di"]-data1["ci"])
        RS_var= data1["RS"].groupby(pd.Grouper(freq='1D')).mean().dropna()
        Vc_and_Vo=data1[["oi", "ci"]].groupby(pd.Grouper(freq='1D')).var().dropna()
        n=int(len(data1)/len(RS_var))
        k = 0.34/(1.34+(n+1)/(n-1))
        Yang_Zhang_RV=np.sqrt((1-k)*RS_var+Vc_and_Vo["oi"]+Vc_and_Vo["ci"]*k)
        Yang_Zhang_RV_df=pd.DataFrame(Yang_Zhang_RV)
        Yang_Zhang_RV_df.rename(columns={0: "Yang & Zhang RV proxy"},inplace=True)
        Multivariate_Yang_Zhang_RV.append(Yang_Zhang_RV_df)
    
    return Multivariate_Yang_Zhang_RV