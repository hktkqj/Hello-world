#!/bin/bash 
<<PROXY_SETTING
echo 'Initializing proxy configuration...'
http_proxy="" curl -I www.google.com.hk > /dev/null
if [ $? -eq 0 ] 
then
    echo 'Proxy already set.'
else
    proxy_suc=0
    while [ $proxy_suc -eq 0 ]
    do
        echo 'Proxy unavailable, please enter your credit.'
        echo 'Enter your domain username:'
        read domain_username
        echo 'Enter your domain password:'
        read domain_password
        http_construct="http://${domain_username}:${domain_password}@proxy.huawei.com:8080"
        https_construct="https://${domain_username}:${domain_password}@proxy.huawei.com:8080"
        http_proxy=${http_construct} curl -I www.google.com.hk > /dev/null
        if [ $? -eq 0 ]
        then
            echo 'Proxy available, writing to ~/.bashrc'
            echo "export http_proxy=${http_construct}" >> ~/.bashrc
            echo "export https_proxy=${https_construct}" >> ~/.bashrc
            proxy_suc=1
        fi
    done
fi
echo "Proxy configuration complete. Cleaning..."
sleep 3
clear
PROXY_SETTING

<<ALIAS_SETTING
echo 'Adding alias l=ls, ll=ls -al, cls=clear to ~/.bashrc'
echo "alias l='ls'" >> ~/.bashrc
echo "alias ll='ls -al'" >> ~/.bashrc
echo "alias cls='clear'" >> ~/.bashrc
echo "Alias adding complete. Cleaning..."
sleep 3
clear
ALIAS_SETTING

# System code: Kali = 0, Ubuntu = 1

<<SOURCE_EDIT
sys_info=`uname -a`
if [[ $sys_info =~ 'kali' ]]
then
    sys_code=0
    echo 'Kali Linux detected. Adding mirrors...'
    mv /etc/apt/sources.list /etc/apt/sources.list.bak
    echo 'Old source backup in /etc/apt/sources.list.bak'
    echo "# These source was created by configuration script" > /etc/apt/sources.list
    echo "deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
    while true
    do
        read -r -p "Add source packages ?(may affect update&&upgrade speed) [y/N]" input
        case $input in
            [yY][eE][sS]|[yY])
                echo "" 
                echo "# Source packages below "
                echo "deb-src https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
                echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
                break
                ;;

            [nN][oO]|[nN])
                break 	
                ;;

            *)
                break
                ;;
        esac
    done
elif [[ $sys_info =~ 'ubuntu' ]]
then
    sys_code=1
    echo 'Ubuntu detected. Adding mirrors...'
    sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
    echo 'Old source backup in /etc/apt/sources.list.bak'
    echo "# These source was created by configuration script" > /etc/apt/sources.list
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
    while true
    do
        read -r -p "Add source packages ?(may affect update&&upgrade speed) [y/N]" input
        case $input in
            [yY][eE][sS]|[yY])
                echo "" 
                echo "# Source packages below "
                echo "deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list
                echo "deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list
                echo "deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list
                echo "deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
                break
                ;;

            [nN][oO]|[nN])
                break 	
                ;;

            *)
                break
                ;;
        esac
    done
fi
echo "APT config complete. Cleaning..."
sleep 3
clear
SOURCE_EDIT

<<APT_UP
echo "Cleaning prompts..."
sleep 3
clear 
echo "Prompt cleaned, executing apt update && upgrade....(May take a long time)"
echo "Please follow the instruct if configuration required."
sleep 3
apt update 2>&1 | tee apt_update.log
if [ $sys_code -eq 0 ]
then
    echo "Kali detected, automatically hold inetsim, laudanum, mimikatz, powersploit, responder, sbd, sqldict, wce, webshells"
    apt-mark hold inetsim laudanum mimikatz powersploit responder sbd sqldict wce webshells
fi
sleep 3
apt upgrade -y 2>&1 | tee apt_upgrade.log
if [ $? -eq 0 ]
then
    echo "Upgrade sucessfully. Autoremove extra packages."
else
    echo "Exception meeted, please view logfile then manually execute apt update && apt upgrade."
fi
sleep 3
apt autoremove -y
APT_UP

<<VSCODE_INS
mkdir install_packages
wget https://go.microsoft.com/fwlink/?LinkID=760868 --no-check-certificate -O ./install_packages/vscode_install.deb 
if [ $? -ne 0 ]
then 
    echo "Unable to install VSCode, please visit https://code.visualstudio.com/ and download manually."
else
    echo "Installing VSCode..."
    sleep 3
    #dpkg -i ./install_packages/vscode_install.deb
    sleep 1
    echo "Successfully installed VSCode."
    sleep 3
    while true
    do
        read -r -p "Download && install extra plugins?(C++/Python/Markdown/Language Pack) [y/N]" input
        case $input in
            [yY][eE][sS]|[yY])
                wget https://github.com/microsoft/vscode-cpptools/releases/download/0.25.0/cpptools-linux.vsix --no-check-certificate -O ./install_packages/cpp_plugin.vsix
                wget https://github.com/microsoft/vscode-python/releases/download/2019.8.30787/ms-python-release.vsix --no-check-certificate -O ./install_packages/py_plugin.vsix
                wget https://github.com/yzhang-gh/vscode-markdown/releases/download/beta/markdown-all-in-one-1.3.0-0519.vsix --no-check-certificate -O ./install_packages/md_plugin.vsix
                # Too bad that I can't find a direct link for zh-hans language plugin
                /usr/bin/code --usre-data-dir ~/ --install-extension ./install_packages/cpp_plugin.vsix --user-data-dir 
                /usr/bin/code --usre-data-dir ~/ --install-extension ./install_packages/py_plugin.vsix --user-data-dir 
                /usr/bin/code --usre-data-dir ~/ --install-extension ./install_packages/md_plugin.vsix --user-data-dir 
                /usr/bin/code --usre-data-dir ~/ --install-extension ./install_packages/zh_hans_extension.vsix- -user-data-dir 
                echo "Plugin install complete..."
                sleep 3
                clear
                echo "Installing pylint..."
                pip install pylint
                pip3 install pylint
                echo -e "{\n    \"locale\": \"zh-cn\"\n}"  > ~/.config/Code/User/locale.json
                echo "VSCode configuration complete."
                break
                ;;

            [nN][oO]|[nN])
                break 	
                ;;

            *)
                break
                ;;
        esac
    done
fi
echo "VSCode configuration complete. Cleaning..."
sleep 3
clear
VSCODE_INS


