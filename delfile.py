#
#
#
import os
import glob
import datetime

# 現在時刻をepochで取得
now = int(datetime.datetime.now().strftime('%s'))

# 対象ディレクトリと拡張子を取得
with open('/home/pi/program/delfile/info.txt', 'r') as fr:
    line = fr.readline()
line = line.split(',')
path = line[0]
ext  = line[1]

# 対象ファイルのepoch時を取得
for delfile in glob.glob(path + '*.' + ext):
    stat = int(os.stat(delfile).st_mtime)    
    # 10分以上前のファイルの場合は削除
    if stat + 600 <= now:
        print('DELETE : ' + delfile)
        os.remove(delfile)

