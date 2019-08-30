using System.Windows;

namespace LanTransfer
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            Window window;

            window = new Server("hello");
            /*
            if (e.Args.Length == 1)
            {
                MessageBox.Show("Now opening file: \n\n" + e.Args[0]);
                window = new Server(e.Args[0]);
            }
            else
            {
                window = new Client();
            }*/

            window.Show();
        }
    }
}
