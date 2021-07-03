# JavaScripts

### boolean

```
console.log(2 < 1 && 'Codeit' !== 'Codeit');
```

2 < 1는 false고, 'Codeit' !== 'Codeit'도 false이기 때문에 이 코드는 false && false가 되어서 실행했을 때 false가 출력
그런데 사실, AND연산을 할 때 왼쪽이 false일 경우 오른쪽은 볼 필요도 없이 결과가 false AND연산은 양쪽이 모두 true인 경우에만 true가 리턴되기 때문
그래서 불린 연산자가 하나만 있을 때는 연산자를 기준으로 왼쪽부터 순서대로 확인하면 됨

```
console.log(7 !== 7 || 4 < 3);
```

OR연산의 경우에는 AND연산과 반대로 왼쪽이 true라면, 오른쪽은 볼 필요도 없이 결과는 true
그런데 마침 OR연산의 왼쪽, 그러니까 7 !== 7이 false이기 때문에 이제 오른편도 확인해야 함
4 < 3은 false이기 때문에 결과적으로 위 연산은 false OR false가 돼서 코드를 실행해보면 false가 출력
