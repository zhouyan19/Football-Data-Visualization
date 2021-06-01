<template>
  <div class="home">
    <el-header>
      <div class="img-box"><img src="@/assets/logo2.png"></div>
      <h1 class="title">Football Data Visualization</h1>
    </el-header>
    <el-container>
      <el-aside class="aside1">
        <Aside
          @to_draw="() => mode='draw'"
          @to_manage="() => mode='manage'"
          @to_search="() => mode='search'"
          @to_rankings="() => mode='rankings'"
        />
      </el-aside>
      <el-main v-if="mode==='draw'">
        <Draw/>
      </el-main>
      <el-main v-if="mode==='manage'">
        <Manage/>
      </el-main>
      <el-main v-if="mode==='search'">
        <Search/>
      </el-main>
      <el-main v-if="mode==='rankings'">
        <Rankings/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Aside from '@/components/Aside'
import Draw from '@/components/Draw'
import Manage from '@/components/Manage'
import Search from '@/components/Search'
import Rankings from '@/components/Rankings'
export default {
  name: 'Home',
  components: {
    Aside,
    Draw,
    Manage,
    Search,
    Rankings
  },
  data () {
    return {
      mode: 'draw',
      data: '',
      form: {
      }
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  /* border: 10px solid rgb(115, 0, 150); */
  background-color: #dcf1fdee;
  min-height: 856px;
}
.home ::-webkit-scrollbar {
  width: 8px;
}
.home ::-webkit-scrollbar-thumb {
  background-color: #eaecf1;
  border-radius: 3px;
}
.el-container {
  display: flex;
  /* border: 10px solid rgb(8, 158, 20); */
  min-height: 640px;
  align-items: stretch;
  background-color: #dcf1fdee;
}
.el-main {
  display: flexbox;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  min-height: 720px;
  background-color: #ffffffee;
  margin-left: 40px;
  margin-right: 40px;
  /* border: 10px solid rgb(247, 38, 1); */
}
.main {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: flex-start;
  align-items: stretch;
  min-height: 720px;
  background-color: #dcf1fdee;
  /* border: 10px solid rgb(202, 25, 25); */
}
.el-header, .el-footer {
  /* border: 1px solid rgb(0, 0, 0); */
  display: flex;
  justify-content: flex-start;
  align-items: center;
  background-color: #4399fcd5;
  color: rgb(250, 250, 250);
  text-align: center;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 90px;
  z-index: 100;
  position: relative;
  margin-bottom: 40px;
}
.title {
  margin-left: 30px;
}
.img-box {
  max-width: 200px;
}
.aside1 {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
  margin-left: 40px;
  border: 0px solid transparent;
  border-radius: 0px;
  background-color: rgb(250, 250, 250);
  color: #070707;
  width: 200px;
}
</style>
