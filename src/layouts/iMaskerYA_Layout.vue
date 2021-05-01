<template>
  <q-layout view="hHh Lpr lff">
    <q-header elevated >
      <q-toolbar style="background-color:#1a1a1a; height:20%;">
        <q-btn
          flat
          dense
          round
          size="22px"
          icon="list"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          <span style="font-size:26px;"> iMaskerYA </span> 
          <span v-if="route_path=='/dashboard'" style="color:#3CB371; font-weight:bold; font-family:Microsoft JhengHei; font-size:26px;"> Dashboard </span>
          <span v-if="route_path=='/history'" style="color:#3CB371; font-weight:bold; font-family:Microsoft JhengHei; font-size:26px;"> History </span>
        </q-toolbar-title>
        <q-space />
        <q-img src="../images/mask_logo.png"  style="height:auto-fill; width:3%;"/>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"

      :width="200"
      :breakpoint="500"
      content-class="bg-grey-1"
      style="font-family:Microsoft JhengHei; font-weight:bold;"
    >
      <q-list>

        <q-item clickable v-ripple to='/dashboard' style="height:60px">
          <q-item-section avatar>
            <q-icon name="dashboard" />
          </q-item-section>

          <q-item-section>
            <span style="font-size:1.2em;">主頁面</span>
            <span style="color:grey; font-size: 0.9em;">Dashboard</span>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to='/history' style="height:60px">
          <q-item-section avatar>
            <q-icon name="history" />
          </q-item-section>

          <q-item-section>
            <span style="font-size:1.2em;">歷史資料</span>
            <span style="color:grey; font-size: 0.9em;">History</span>
          </q-item-section>
        </q-item>

      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer style="background-color:transparent">
      <div class="text-right" style="color:lightgrey">
        NTPU MIS, Huang Chun Yu 
      </div>
    </q-footer>

  </q-layout>
</template>

<script>

export default {
  name: 'MainLayout',
  components: { },
  data () {
    return {
      route_path: '',
      miniState: true,
      leftDrawerOpen: false,
    }
  },
  created(){
    this.route_path = this.$route.path
  },
  watch:{
    $route (to, from){
      this.route_path = this.$route.path
    }
  }
}
</script>
