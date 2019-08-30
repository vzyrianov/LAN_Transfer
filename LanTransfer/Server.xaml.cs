using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Windows;

namespace LanTransfer
{
    /// <summary>
    /// Interaction logic for Server.xaml
    /// </summary>
    public partial class Server : Window
    {
        class PotentialAddress
        {
            public PotentialAddress(string ip)
            {
                IP = ip;
            }

            public string IP { get; private set; }
        }

        private string filepath;
        private TcpClient connection;
        private ObservableCollection<PotentialAddress> potentialAddresses;

        public Server(string path)
        {
            filepath = path;
            potentialAddresses = new ObservableCollection<PotentialAddress>();
            potentialAddresses.Add(new PotentialAddress("192.16.1.1"));
            InitializeComponent();
            dataGrid.DataContext = potentialAddresses;
        }

        void WaitForConnections()
        {
            var server = new UdpClient(8888);
            var responseData = Encoding.ASCII.GetBytes("accepted");

            while (true)
            {
                var clientEndPoint = new IPEndPoint(IPAddress.Any, 0);
                var clientRequestData = server.Receive(ref clientEndPoint);
                var clientRequest = Encoding.ASCII.GetString(clientRequestData);

                server.Send(responseData, responseData.Length, clientEndPoint);
                potentialAddresses.Add(new PotentialAddress(clientEndPoint.Address.ToString()));
            }
        }
    }
}
