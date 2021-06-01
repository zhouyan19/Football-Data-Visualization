<template>
  <div class="manage">
    <h1 style="font-size:32px">Competition Management</h1>
    <el-container class="all_board">
      <el-tabs v-model="field" @tab-click="tabClick">
        <el-tab-pane name="add">
          <span slot="label" style="font-size:16px">ADD</span>
          <div class="content" v-if="update1"><MAdd/></div>
        </el-tab-pane>
        <el-tab-pane name="edit">
          <span slot="label" style="font-size:16px">EDIT</span>
          <div class="content" v-if="update3"><MEdit/></div>
        </el-tab-pane>
        <el-tab-pane name="delete">
          <span slot="label" style="font-size:16px">DELETE</span>
          <div class="content" v-if="update2"><MDelete/></div>
        </el-tab-pane>
        <el-tab-pane name="query">
          <span slot="label" style="font-size:16px">QUERY</span>
          <div class="content" v-if="update4"><MQuery/></div>
        </el-tab-pane>
      </el-tabs>
    </el-container>
  </div>
</template>

<script>
import MAdd from '@/components/MAdd'
import MDelete from '@/components/MDelete'
import MEdit from '@/components/MEdit'
import MQuery from '@/components/MQuery'
export default {
  name: 'Manage',
  components: {
    MAdd,
    MDelete,
    MEdit,
    MQuery
  },
  data () {
    return {
      field: 'add', // add, delete, edit, query
      update1: true,
      update2: false,
      update3: false,
      update4: false
    }
  },
  methods: {
    tabClick (tab) {
      if (tab.name === 'add') {
        this.update1 = true
        this.update2 = false
        this.update3 = false
        this.update4 = false
      } else if (tab.name === 'delete') {
        this.update1 = false
        this.update2 = true
        this.update3 = false
        this.update4 = false
      } else if (tab.name === 'edit') {
        this.update1 = false
        this.update2 = false
        this.update3 = true
        this.update4 = false
      } else { // query
        this.update1 = false
        this.update2 = false
        this.update3 = false
        this.update4 = true
      }
    }
  }
}
</script>

<style scoped>
.manage {
  height: 100%;
  box-sizing: border-box;
  border: 0px solid rgba(131, 131, 131, 0.596);
  border-radius: 8px;
  margin-left: 40px;
  margin-top: -20px;
}
.all_board {
  margin-top: -10px;
}
.content {
  margin-top: 30px;
}
</style>
