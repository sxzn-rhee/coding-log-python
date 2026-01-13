# 01 - import / as / from 실습
## 실행 명령어 
```bash 
python3 snippets/01_import_as_from/example.py
```
### 실행 결과 
1. import math -> math.sqrt(9):3.0
2. from math import sqrt -> sqrt(16):4.0
3. import datetime as dt -> now:(실행할 때마다 달라짐)

### 포인트 
- import math: 모듈을 통째로 가져와 math.sqrt()처럼 사용
- from math import sqrt: 함수만 꺼내와 sqrt()로 바로 사용
- import datetime as dt: alias(별명)로 짧게 사용
-
```bash
if __name__ == "__main__":
``` 
 직접 실행할 때만 main() 실행