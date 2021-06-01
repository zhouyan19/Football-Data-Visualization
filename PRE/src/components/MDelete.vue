<template>
  <div class="manage_delete">
    <el-container class="all_board">
      <div class="tips"> *Tips: Only to delete the latest one.</div>
      <div class="button_box">
        <el-button
          type="danger"
          @click="submit"
          style="font-size:20px"
          icon="el-icon-delete"
        >
          Delete
        </el-button>
      </div>
    </el-container>
  </div>
</template>

<script>
import {deleteGame} from '@/utils/communication'
export default {
  name: 'MDelete',
  methods: {
    submit () {
      deleteGame().then((successful) => {
        if (successful) {
          this.$message({
            type: 'success',
            message: 'Delete successfully！'
          })
        } else {
          this.$message({
            type: 'error',
            message: 'Error！'
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.tips {
  font-size: 20px;
  margin-bottom: 50px;
  margin-top: 10px;
}
.button_box {
  margin-left: 120px;
}
</style>
