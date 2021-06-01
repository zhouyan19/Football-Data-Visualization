<template>
  <div class="my-aside">
    <el-col :span="16">
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo">
        <el-menu-item index="1"
          @click="$emit('to_draw', {})">
          <i class="el-icon-picture"></i>
          Visualization
        </el-menu-item>
        <el-menu-item index="2"
          @click="$emit('to_manage', {})">
          <i class="el-icon-football"></i>
          Competitions
        </el-menu-item>
        <el-menu-item index="3"
          @click="$emit('to_search', {})">
          <i class="el-icon-search"></i>
          Search Team
        </el-menu-item>
        <el-menu-item index="4"
          @click="$emit('to_rankings', {})">
          <i class="el-icon-s-data"></i>
          Rankings
        </el-menu-item>
      </el-menu>
    </el-col>
  </div>
</template>

<script>
export default {
  name: 'Aside'
}
</script>

<style scoped>
.el-menu-vertical-demo {
  margin-top: 40px;
}
.my-aside {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
  background-color: transparent;
  overflow-y: auto;
  overflow-x: hidden;
  border: 0px solid transparent;
  margin-left: 30px;
}
.el-menu {
  background-color: transparent;
  border: 0px solid transparent;
}
.el-menu-item {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  width: 200px;
  color: rgb(0, 0, 0);
  border: 0px solid transparent;
}
.el-menu-item.is-active {
  background-color: rgba(166, 207, 255, 0.877) !important;
  color: rgb(0, 0, 0);
}
.el-menu-item:hover {
  background-color: rgba(200, 229, 255, 0.623) !important;
  color: rgb(0, 0, 0);
}
.el-col {
  display: flex;
  flex-direction: column;
  height: 90%;
  float: 1 0 auto;
}
.el-footer {
  /* border: 1px solid rgb(0, 0, 0); */
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  background-color: transparent;
  color: rgb(255, 255, 255);
  top: 0;
  left: 0;
  width: 100%;
  line-height: 20px;
  font-size: small;
  float: 0 0 auto;
  position: relative;
}
</style>
