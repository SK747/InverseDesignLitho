import paramiko
import scp

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hydra1.ece.ubc.ca', username='mustafa')

# SCPCLient takes a paramiko transport as its only argument
scp_client = scp.SCPClient(ssh.get_transport())

# Send input.gds file
scp_client.put('input.gds', '/ubc/ece/home/nano/data/LC_GROUP/Lithography_Model_V4_Published')

print('ive arrived here')

# Execute the shell script
ssh.exec_command('cd /ubc/ece/home/nano/data/LC_GROUP/Lithography_Model_V4_Published && source run_litho.sh')

print('ive arrived here') 

# Get the results file
scp_client.get('/ubc/ece/home/nano/data/LC_GROUP/Lithography_Model_V4_Published/results.gds', 'results10.gds')

# Close connections
scp_client.close()
ssh.close()