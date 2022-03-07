#!/usr/bin/python3
import speedtest 
import logging 
import time

def main():
    st = speedtest.Speedtest()
    while True:
        st.get_servers()
        st.get_best_server() 
        ping = st.results.ping 
        download = st.download()
        upload = st.upload()
        print(f"{time.time()},{download},{upload},{ping}")
        time.sleep(5*60)

if __name__ == '__main__':
    main()
