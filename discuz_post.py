#coding:utf-8
import time
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect("localhost","root","test","juben")
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')

title = MySQLdb.escape_string('title2')
content = MySQLdb.escape_string('content2')
att_name = MySQLdb.escape_string('att_name.txt')

cursor.execute("SELECT max(tid) FROM forum_thread")
tid = int(cursor.fetchone()[0]) + 1
cursor.execute("SELECT max(pid) FROM forum_post")
pid = int(cursor.fetchone()[0]) + 1
cursor.execute("SELECT max(aid) FROM forum_attachment")
aid = int(cursor.fetchone()[0]) + 1

cursor.execute("INSERT INTO forum_thread SET `fid`='2' , `tid`='" + str(tid) + "' , `posttableid`='0' , `readperm`='0' , `price`='0' , `typeid`='0' , `sortid`='0' , `author`='admin' , `authorid`='1' , `subject`='" + title + "' , `dateline`='" + str(int(time.time())) + "' , `lastpost`='" + str(int(time.time())) + "' , `lastposter`='admin' , `displayorder`='0' , `digest`='0' , `special`='0' , `attachment`='1' , `moderated`='0' , `status`='32' , `isgroup`='0' , `replycredit`='0' , `closed`='0'")
cursor.execute("INSERT INTO forum_newthread SET `tid`='" + str(tid) + "' , `fid`='2' , `dateline`='" + str(int(time.time())) + "'")
cursor.execute("INSERT INTO forum_post_tableid SET `pid`='" + str(pid) + "'")
cursor.execute("INSERT INTO forum_post SET `fid`='2' , `tid`='" + str(tid) + "' , `first`='1' , `author`='admin' , `authorid`='1' , `subject`='" + title + "' , `dateline`='" + str(int(time.time())) + "' , `message`='" + content + "' , `useip`='140.112.218.141' , `port`='11560' , `invisible`='0' , `anonymous`='0' , `usesig`='1' , `htmlon`='0' , `bbcodeoff`='-1' , `smileyoff`='-1' , `parseurloff`=0 , `attachment`='1' , `tags`='' , `replycredit`='0' , `status`='0' , `pid`='" + str(pid) + "'")
cursor.execute("UPDATE common_stat SET `thread`=`thread`+1 WHERE `daytime` = '" + time.strftime("%Y%m%d") + "'")
cursor.execute("UPDATE forum_forum SET threads=threads+'1', posts=posts+'1', todayposts=todayposts+'1' WHERE `fid`='2'")
cursor.execute("INSERT INTO forum_sofa SET `tid`='" + str(tid) + "' , `fid`='2'")
cursor.execute("INSERT INTO forum_attachment_" + str(aid % 10) + " SET `readperm`='0' , `price`='10' , `tid`='" + str(tid) + "' , `pid`='" + str(pid) + "' , `uid`='1' , `description`='' , `aid`='" + str(aid) + "' , `dateline`='" + str(int(time.time())) + "' , `filename`='" + att_name + "' , `filesize`='4' , `attachment`='upload/" + att_name + "' , `remote`='0' , `isimage`='0' , `width`='0' , `thumb`='0'")
cursor.execute("INSERT INTO forum_attachment SET `tid`='" + str(tid) + "' , `pid`='" + str(pid) + "' , `tableid`='" + str(aid % 10) + "', `aid`='" + str(aid) + "'")
print 'done'