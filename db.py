#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:14:06 2017

@author: dm
"""

import pymysql
import cmd

conn= pymysql.connect(host='127.0.0.1',user='root',password='abcd',db='salongier')

class db(cmd.Cmd):
    
    
    #a=conn.cursor()


    def do_wypiszGry(self, args):
    
        cur = conn.cursor()    

        sql = "SELECT * FROM Gry"

        cur.execute(sql)

        #print(cur.fetchall())

        for gry in cur.fetchall():
            print(gry)
        
        
    #options = { 1 : one()}

    #num = input("wpisz numerek : " )
    #print(num)

    #if num == '1':
        #one()
        
    def do_wypiszGraczy(self, args):
        
        cur = conn.cursor()    

        sql = "SELECT * FROM Gracze"

        cur.execute(sql)

        #print(cur.fetchall())

        for gry in cur.fetchall():
            print(gry)
    
        
    def do_wypiszWyniki(self, args):
        
        cur = conn.cursor()    

        sql = "SELECT * FROM Wyniki"

        cur.execute(sql)

        #print(cur.fetchall())

        for i in cur.fetchall():
            print(i)
            
    def do_topGraczy(self, args):
        
        cur = conn.cursor()
        
        sql = "select count(id_gracza) as liczba_wynikow, imie, nazwisko from Gry natural join Wyniki natural join Gracze group by id_gracza order by liczba_wynikow DESC ;"
        
        cur.execute(sql)
        
        for i in cur.fetchall():
            print(i)
            
    def do_highScores(self, args):
        
        cur = conn.cursor()
        
        sql = "select sum(wynik) as laczny_wynik, imie, nazwisko from Gry natural join Wyniki natural join Gracze group by id_gracza order by laczny_wynik DESC ;"

        cur.execute(sql)
        
        for i in cur.fetchall():
            print(i)
       
    def do_highScore(self, args):
        
        cur = conn.cursor()
        
        sql = "select nazwa, imie, nazwisko, wynik from Gry natural join Wyniki natural join Gracze where id_gry = %s  order by wynik DESC" ;

        #print(args)
        cur.execute(sql, args)
        
        
        
        for i in cur.fetchall():
            print(i)
            
    def do_topGry(self, args):
        cur = conn.cursor()
        
        sql = "select count(id_gry) as liczba_gran, nazwa from Gry natural join Wyniki natural join Gracze group by id_gry order by liczba_gran DESC;"

        
        cur.execute(sql)
        
        for i in cur.fetchall():
            print(i)
            
    def do_topWyniki(self, args):
        
        cur = conn.cursor()
        
        sql = "select nazwa, imie, nazwisko, wynik from Gry natural join Wyniki natural join Gracze  order by wynik DESC ;"

        
        cur.execute(sql)
        
        for i in cur.fetchall():
            print(i)
            
    def do_quit(self,args):
        
        raise SystemExit
            
            
if __name__ == '__main__':
    PROMPT = db()
    PROMPT.prompt = '(db) '
    PROMPT.cmdloop('wprowadz komende(lista dostepnych komend : help)')