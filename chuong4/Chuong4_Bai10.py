import time

hinh1 = """
      *
      * *
      * * *
* * * * * * *
* * *
* *
*
"""

hinh2 = """
      *
      * *
      *   *
* * * * * * *
*   *
* *
*
"""

hinh3 = """
      * * * *
      * * *
      * *
      *
    * * 
  * * *
* * * *
"""

hinh4 = """
      * * * *
      *   *
      * *
      *
    * * 
  *   *
* * * *
"""

ds_hinh = [hinh1, hinh2, hinh3, hinh4]
for hinh in ds_hinh:
    print(hinh)
    time.sleep(5)