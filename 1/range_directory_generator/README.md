# range_directory_generator

This program is a python program that creates the desired number of folders in the path you want.



## How to use?

python range_directory_generator -h     < help >
python range_directory_generator --path=/foo/bar/test --count=100   

<--path : Enter the path to the directory.>
<--count : Enter the number of subdirectories. (default = 1)>


## What I learned?

* except를 쓸 때는 except: 만 쓰는게 아니라<br/><br/> 
  except <exception name> :<br/>
        …		이렇게 단독으로 처리하거나<br/>

   os.makedirs(dirname, exist_ok=True) 이렇게 하거나 둘중 하나로 해야함
  
  <br/>
* 프로그래밍은 기본적으로 중복이 나오지 않게 해야한다.
  * import argparse을 사용하여 매개변수 값을 입력하여 코드를 또 수정할 일이 없도록 한다

  
  <br/>
* 경로를 쓸때는 \ 보단 / 를 사용하는 것이 윈도우와 리눅스 둘 다 호환이 된다. ( 개발은 보통 리눅스로 하니까 /로 하는 것이 좋다.)
  
  * ex)   /foo/bar (o)             \foo\bar  (x)

  
  <br/>
* 주석은 가능하면 안쓰고 코드로 이해시키는 것이 클린코드이다.
  * 주석을 써야한다면 코드의 윗줄에 쓰는 것이 좋다 ( 변수명이 중요하다.)
  
  * 현업에서는 docstring을 사용한다.
  
  ex) # 주석주석주석주석\
      print('프린트')

* 파일명도 직관적으로 무슨 기능을 하는지 이해하기 쉽게 만들어야 한다.
  

<br/>
* import argparse 사용 중에 어려웠던 점
  \nparser = argparse.ArgumentParser(
    description=
    '''
    == Please enter a folder path. ==
    ex) --path=C:\dir1\dir2\dir3\<name>
    
    == Please enter the number of folders to create. ==
    ex) --count=10    
    '''
)
<br/>
이것을 설명을 깔끔하게 보이려고 ''' '''을 썻지만 
줄 바꿈을 무시했다

parser = argparse.ArgumentParser(description=<br/>
'''<br/>
--path : Enter the path to the directory.<br/>
    
--count : Enter the number of subdirectories.<br/>           
''',<br/>
    formatter_class=argparse.RawTextHelpFormatter<br/>
)<br/>

 formatter_class=argparse.RawTextHelpFormatter 이걸 넣어서 해결

  
  
