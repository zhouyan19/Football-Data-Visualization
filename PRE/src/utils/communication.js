import API from './API'

export const getInfo = (e, n, d1, d2) => fetch(
  API.GET_INFO.path + '?event=' + String(e) + '&name=' + String(n) + '&date1=' + String(d1) + '&date2=' + String(d2),
  { method: API.GET_INFO.method }
).then((res) => res.json()).then((r) => r.data)

export const addGame = (jsonGame) => fetch(API.ADD_GAME.path, {
  method: API.ADD_GAME.method,
  body: JSON.stringify(jsonGame),
  headers: {'Content-Type': 'application/json'}
}).then((res) => res.json()).then((r) => r.code === 200)

export const editGame = (jsonGame) => fetch(API.EDIT_GAME.path, {
  method: API.EDIT_GAME.method,
  body: JSON.stringify(jsonGame),
  headers: {'Content-Type': 'application/json'}
}).then((res) => res.json()).then((r) => r.code === 200)

export const deleteGame = () => fetch(API.DELETE_GAME.path, {
  method: API.DELETE_GAME.method,
  body: '',
  headers: {'Content-Type': 'application/json'}
}).then((res) => res.json()).then((r) => r.code === 200)

export const getGames = (t, n, d1, d2, r) => fetch(
  API.QUERY_GAME.path + '?tournament=' + String(t) + '&name=' + String(n) + '&date1=' + String(d1) + '&date2=' + String(d2) + '&result=' + String(r),
  { method: API.QUERY_GAME.method }
).then((res) => res.json()).then((r) => r.data)

export const getRanking = (t) => fetch(
  API.GET_RANK.path + '?rank_type=' + String(t),
  { method: API.GET_RANK.method }
).then((res) => res.json()).then((r) => r.data)
