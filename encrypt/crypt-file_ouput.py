ActivePython 2.7.2.5 (ActiveState Software Inc.) based on
Python 2.7.2 (default, Jun 24 2011, 12:21:10) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> # Testing for assign7, q. 6
>>> encryptToFile(text, 9, 'crypt_text.txt')
>>> open('crypt_text.txt').read()
'<M\rPujU\x03.\rq\x01\x1bf\x1e\x0e+\x05qa\n+\x02&{>\x11-\x0c\x008V)o&HSwPsy\rQ\x10\x0c\x14y\x05\x1dq6~m{\x1fb[X\x0f|4\x0e\x0f\x15qz\x04\x14&rd?\x17[\x1e\nrCLy+zHJzg\x07i\x02w1t_)a@\x00\x0f\x006{vnG$7"c h\x13\x00ND\x0f!;7vh\x1b\x12k\x01$w(I\x01eC\x13\x05\x17|.\x19rg\x196\x02H\x19 8Th\t{\'$\n\x023Yf\x12\x15|S o\x12nWncF\x7fo\x7fM1\rqm\x1c |![c\x16.{RF[?\x1c\x04E*z\x11M\\z\x16<\x1b\x00R]|{fB-yY\x034\x1cI\x04>[7\x17(\r\x0bU\'\x7f'
>>> text
'Emission of greenhouse gases is a serious issue in the world as climate change becomes more prominent. However, reduction of greenhouse gases emission will be most effective if changes are made at the lowest level; the people. '
>>> decryptToFile(text, 9, 'crypt_text.txt')
Emission of greenhouse gases is a serious issue in the world as climate change becomes more prominent. However, reduction of greenhouse gases emission will be most effective if changes are made at the lowest level; the people. 
>>> 
