#coding:utf-8 #
import MySQLdb
db = MySQLdb.connect("localhost","root","test","juben")
NUMBER = 1
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')
total_number = 1001
while total_number <= 2620:
    file = open(str(total_number) + '.txt')
    origin_title = file.readline()
    title = MySQLdb.escape_string(origin_title[:60])
    file.readline()
    picture = file.readline()
    content = file.read()
    content = '[img]' + picture + '[/img]' + content
    content = MySQLdb.escape_string(content)
    try:
        cursor.execute("INSERT INTO forum_thread SET `fid`='2' , `tid`='"+str(NUMBER)+"' , `posttableid`='0' , `readperm`='0' , `price`='0' , `typeid`='0' , `sortid`='0' , `author`='admin' , `authorid`='1' , `subject`='"+title+"' , `dateline`='1513136068' , `lastpost`='1513136068' , `lastposter`='admin' , `displayorder`='0' , `digest`='0' , `special`='0' , `attachment`='0' , `moderated`='0' , `status`='32' , `isgroup`='0' , `replycredit`='0' , `closed`='0'")
    except:
        title = MySQLdb.escape_string(origin_title[:61])
        try:
            cursor.execute("INSERT INTO forum_thread SET `fid`='2' , `tid`='" + str(NUMBER) + "' , `posttableid`='0' , `readperm`='0' , `price`='0' , `typeid`='0' , `sortid`='0' , `author`='admin' , `authorid`='1' , `subject`='" + title + "' , `dateline`='1513136068' , `lastpost`='1513136068' , `lastposter`='admin' , `displayorder`='0' , `digest`='0' , `special`='0' , `attachment`='0' , `moderated`='0' , `status`='32' , `isgroup`='0' , `replycredit`='0' , `closed`='0'")
        except:
            title = MySQLdb.escape_string(origin_title[:62])
            cursor.execute("INSERT INTO forum_thread SET `fid`='2' , `tid`='" + str(NUMBER) + "' , `posttableid`='0' , `readperm`='0' , `price`='0' , `typeid`='0' , `sortid`='0' , `author`='admin' , `authorid`='1' , `subject`='" + title + "' , `dateline`='1513136068' , `lastpost`='1513136068' , `lastposter`='admin' , `displayorder`='0' , `digest`='0' , `special`='0' , `attachment`='0' , `moderated`='0' , `status`='32' , `isgroup`='0' , `replycredit`='0' , `closed`='0'")

    cursor.execute("INSERT INTO forum_newthread SET `tid`='"+str(NUMBER)+"' , `fid`='2' , `dateline`='1513135706'")
    cursor.execute("INSERT INTO forum_post_tableid SET `pid`='"+str(NUMBER)+"'")
    cursor.execute("INSERT INTO forum_post SET `fid`='2' , `tid`='"+str(NUMBER)+"' , `first`='1' , `author`='admin' , `authorid`='1' , `subject`='"+title+"' , `dateline`='1513136068' , `message`='"+content+"' , `useip`='140.112.218.141' , `port`='11560' , `invisible`='0' , `anonymous`='0' , `usesig`='1' , `htmlon`='0' , `bbcodeoff`='0' , `smileyoff`='-1' , `parseurloff`=0 , `attachment`='0' , `tags`='' , `replycredit`='0' , `status`='0' , `pid`='"+str(NUMBER)+"'")
    cursor.execute("UPDATE common_stat SET `thread`=`thread`+1 WHERE `daytime` = '20171213'")
    cursor.execute("UPDATE forum_forum SET threads=threads+'1', posts=posts+'1', todayposts=todayposts+'1' WHERE `fid`='2'")
    cursor.execute("INSERT INTO forum_sofa SET `tid`='"+str(NUMBER)+"' , `fid`='2'")
    cursor.execute("INSERT INTO forum_attachment_"+str(NUMBER%10)+" SET `readperm`='0' , `price`='10' , `tid`='"+str(NUMBER)+"' , `pid`='"+str(NUMBER)+"' , `uid`='1' , `description`='' , `aid`='"+str(NUMBER)+"' , `dateline`='1513135665' , `filename`='全剧本.zip' , `filesize`='4' , `attachment`='201712/13/"+str(total_number)+".zip' , `remote`='0' , `isimage`='0' , `width`='0' , `thumb`='0'")
    cursor.execute("INSERT INTO forum_attachment SET `tid`='"+str(NUMBER)+"' , `pid`='"+str(NUMBER)+"' , `tableid`='"+str(NUMBER%10)+"', `aid`='"+str(NUMBER)+"'")
    cursor.execute("UPDATE  forum_thread SET `attachment`='1' WHERE `tid`='"+str(NUMBER)+"'")
    cursor.execute("UPDATE  forum_post SET `attachment`='1' WHERE `pid`='"+str(NUMBER)+"'")

    NUMBER += 1
    total_number += 1

    print total_number, title
    #break