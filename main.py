import sys
import time
from tools import (netkhat,
                   proxy,
                   sniffer,
                   sniffer_ip_header_decode,
                   ssh_cmd,
                   ssh_rcmd,
    # ssh_server,  <--- not working atm !!!
                   tcp_client,
                   tcp_server,
                   tcpattack,
                   udp_client,
                   mail_sniffer)

availableTools = ["netkhat",
                  "proxy",
                  "sniffer",
                  "sniffer_ip_header_decode",
                  "ssh_cmd",
                  "ssh_rcmd",
                  "ssh_server",
                  "tcp_client",
                  "tcp_server",
                  "tcpattack",
                  "udp_client",
                  "mail_sniffer"]


def main():
    print("__--__--__--Welcome--__--__--__\n")
    for i in range(len(availableTools)):
        print(str(i) + " : " + availableTools[i])
    print("\n")

    while True:
        try:
            print("Tool selection: ")
            toolSelect = int(input())

            tool_initializers = {
                0: netkhat.init,
                1: proxy.init,
                2: sniffer.init,
                3: sniffer_ip_header_decode.init,
                4: ssh_cmd.init,
                5: ssh_rcmd.init,
                6: None,  # Placeholder for "currently unavailable"
                7: tcp_client.init,
                8: tcp_server.init,
                9: tcpattack.init,
                10: udp_client.init,
                11: mail_sniffer.init,
            }

            if toolSelect in tool_initializers:
                if toolSelect == 6:
                    print("currently unavailable")
                else:
                    tool_initializers[toolSelect]()
                break  # Exit the loop if a valid selection is made
            else:
                print("Invalid tool selection value. Please choose a valid tool.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()
