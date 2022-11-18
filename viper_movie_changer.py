#!/usr/bin/env python3
#-*-coding:utf-8 -*-
#downloader.py @takamitsu hamada 20221118
#mainsite : http://vsrx.work

import sys,os,os.path,json
from urllib.request import urlopen
import subprocess as sp
from threading import Thread
import codecs
try:
    import gi
    gi.require_version("Gtk","3.0")
    from gi.repository import Gtk
except:
    sys.exit(1)

class download_youtube(object):
    def __init__(self):
        gladefile = "viper_movie_changer.ui"
        self.tree = Gtk.Builder()
        self.tree.add_from_file(os.path.dirname(os.path.abspath(__file__)) + "/" + gladefile)
        dic = {
            "on_ok1_clicked" : self.on_ok1_clicked,
            "on_ok2_clicked" : self.on_ok2_clicked,
            "on_close_clicked" : self.on_close_clicked,
            "on_button1_clicked" : self.on_button1_clicked,
            "on_button2_clicked" : self.on_button2_clicked,
            "on_install_driver_clicked" : self.on_install_driver_clicked,
            "on_button111_clicked" : self.on_button111_clicked
        }
        treeObj = self.tree.get_object
        self.tree.connect_signals(dic)
        self.downloader = treeObj("downloader")
        self.hls_url = treeObj("hls_url")
        self.output = treeObj("output")
        self.window = treeObj("ok1")
        self.window = treeObj("ok2")
        self.window = treeObj("close")
        self.window = treeObj("button1")
        self.window = treeObj("button2")
        self.window = treeObj("install_driver")
#        self.fcb1 = treeObj("filechooserbutton1")
        self.entry0 = treeObj("entry0")
        self.entry1 = treeObj("entry1")
        self.combo1 = treeObj("comboboxtext1")
        self.combo2 = treeObj("comboboxtext2")
        self.combo3 = treeObj("comboboxtext3")
        self.combo4 = treeObj("comboboxtext4")
        self.combo5 = treeObj("comboboxtext5")
        self.combo6 = treeObj("comboboxtext6")
        self.window = treeObj("button111")
        self.entry_ffmpeg_input = treeObj("entry_ffmpeg_input")
        self.entry_ffmpeg_output = treeObj("entry_ffmpeg_output")
        self.entry_ffmpeg_start = treeObj("entry_ffmpeg_start")
        self.entry_ffmpeg_end = treeObj("entry_ffmpeg_end")
        self.entry_ffmpeg_framerate = treeObj("entry_ffmpeg_framerate")
        self.window = treeObj("window1")
        self.window.show_all()
        if(self.window):
            self.window.connect("destroy",Gtk.main_quit)
        Gtk.main()
    def on_ok1_clicked(self,widget):
        msg1 = self.downloader.get_text()
        cmd = "./downloader.sh %s" % (msg1)
        sp.call(cmd.strip().split(" "))
    def on_ok2_clicked(self,widget):
        msg1=self.hls_url.get_text()
        msg2=self.output.get_text()
        cmd = "./download_hls.sh %s %s" % (msg1,msg2)
        sp.call(cmd.strip().split(" "))
    def on_button1_clicked(self,widget):
        msg1 = self.entry0.get_text()
        msg2 = self.entry1.get_text()
        if(self.combo1.get_active_text() == "640x480"):
            msg3 = 640
            msg4 = 480
        if(self.combo1.get_active_text() == "768x432"):
            msg3 = 768
            msg4 = 432
        if(self.combo1.get_active_text() == "1024x720"):
            msg3 = 1024
            msg4 = 720
        if(self.combo1.get_active_text() == "1280x720"):
            msg3 = 1280
            msg4 = 720
        if(self.combo1.get_active_text() == "1920x1080"):
            msg3 = 1920
            msg4 = 1080
        if(self.combo2.get_active_text() == "h264_vaapi"):
            msg5 = "h264_vaapi"
        if(self.combo2.get_active_text() == "hevc_vaapi"):
            msg5 = "hevc_vaapi"
        if(self.combo3.get_active_text() == "card0"):
            msg6 = "card0"
        if(self.combo3.get_active_text() == "card1"):
            msg6 = "card1"
        if(self.combo3.get_active_text() == "renderD128"):
            msg6 = "renderD128"
        if(self.combo3.get_active_text() == "renderD129"):
            msg6 = "renderD129"
        if(self.combo4.get_active_text() == "4M"):
            msg7 = "4M"
        if(self.combo4.get_active_text() == "8M"):
            msg7 = "8M"
        if(self.combo4.get_active_text() == "10M"):
            msg7 = "10M"
        if(self.combo4.get_active_text() == "12M"):
            msg7 = "12M"
        if(self.combo4.get_active_text() == "16M"):
            msg7 = "16M"
        if(self.combo4.get_active_text() == "18M"):
            msg7 = "18M"
        if(self.combo4.get_active_text() == "20M"):
            msg7 = "20M"
        if(self.combo5.get_active_text() == "128k"):
            msg8 = "128k"
        if(self.combo5.get_active_text() == "192k"):
            msg8 = "192k"
        if(self.combo5.get_active_text() == "256k"):
            msg8 = "256k"
        if(self.combo5.get_active_text() == "386k"):
            msg8 = "386k"
        if(self.combo5.get_active_text() == "512k"):
            msg8 = "512k"
        if(self.combo6.get_active_text() == "29.97"):
            msg9 = "29.97"
        if(self.combo6.get_active_text() == "60"):
            msg9 = "60"
        cmd = "./qsv_enc.sh %s %s %s %s %s %s %s %s %s" % (msg1,msg2,msg3,msg4,msg5,msg6,msg7,msg8,msg9)
        print(cmd)
        sp.call(cmd.strip().split(" "))
    def on_button2_clicked(self,widget):
        Gtk.main_quit()
#    def on_filechooserbutton1_file_set(self,widget):
#        msg1 = self.fcb1.get_filename()
#        return msg1
    def on_install_driver_clicked(self,widget):
        cmd = "./build_media_driver.sh"
        sp.call(cmd.strip().split(" "))
#ffmpeg
    def on_button111_clicked(self,widget):
        msg1 = self.entry_ffmpeg_input.get_text()
        msg2 = self.entry_ffmpeg_output.get_text()
        msg3 = self.entry_ffmpeg_start.get_text()
        msg4 = self.entry_ffmpeg_end.get_text()
        msg5 = self.entry_ffmpeg_framerate.get_text()
        cmd = "./movie2pics.sh %s %s %s %s %s" % (msg3,msg4,msg5,msg1,msg2)
        sp.call(cmd.strip().split(" "))
    def on_close_clicked(self,widget):
        Gtk.main_quit()
if __name__ == "__main__":
    download_youtube()
