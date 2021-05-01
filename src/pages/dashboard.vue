<template>
  <q-page class="q-pa-lg flex justify-center">

    <q-card v-if="total_detect_number !== '載入中...'" flat class="col-12 q-pa-sm row" style="width: 100%; font-family:Microsoft JhengHei; z-index: 2">
      <img
        class="flex flex-center"
        style="position:absolute; background-position:center center; margin-left:550px; padding-top:100px; z-index: 0; width:45%; height:70%;"
        alt="iMaskerYA"
        src="../images/ntpu_background.gif"
      >

      <div v-if="unmask_number === 0" class="col-12 row flex flex-center" style="background-color:#00cc00">
        <q-img src="../images/mask_good.png"  style="height:auto-fill; width:5%;"/>
        <span class="q-px-lg" style="font-size:3rem; font-weight:bold; color:white;">檢測中，狀況正常。 </span>
      </div>

      <div v-if="unmask_number > 0" class="col-12 row flex flex-center" style="background-color:red">
        <q-img src="../images/unmask_warning.png"  style="height:auto-fill; width:6%;"/>
        <span class="q-px-lg" style="font-size:3rem; font-weight:bold; color:white;">警告！請戴上口罩！ </span>
      </div>

      <q-card-section v-if="total_detect_number !== '載入中...'"  class="col row flex q-pa-xs">
        <iframe align="top" src="http://localhost:8090" title="iMaskerYA Detection" width="640px" height="480px" 
          style="zoom:1;
                 -webkit-transform: scale(0.75);" scrolling='no' frameborder="5"> 
        </iframe>
      </q-card-section>
      
      <q-card-section class="col-5 flex flex-start items-center">
        <div v-if="total_detect_number !== '載入中...'" style="font-size: 30px;">
          <p>總人數　： {{total_detect_number}} 位</p>
          <p>戴口罩　： {{mask_number}} 位</p>
          <p>未戴口罩： <span style="color:red"> {{unmask_number}} </span> 位</p>
        </div>
      </q-card-section>
    </q-card>
    
    <div class="row">
      <q-card flat class="q-pa-lg row col-12" style="width:1000px; height:100px;">
      </q-card>
    </div>

    <div v-if="total_detect_number !== '載入中...'" class="q-pa-md col-12">
      <q-btn v-if="!sound_play" round outline @click="turn_sound_on()" icon="volume_off" class="q-mr-md bg-white text-red"/>
      <q-btn v-if="sound_play" round outline @click="turn_sound_off()" icon="volume_up" class="q-mr-md bg-white text-green"/>

      <q-btn-toggle
        v-model="sound_mode"
        bounded
        color="grey"
        text-color="white"
        toggle-color="primary"
        toggle-text-color="white"
        :options="[
          {label: '一般', value: 'normal', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'},
          {label: '溫柔', value: 'kind', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'},
          {label: '罩口業', value: 'shouting', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'}
        ]"
      />
    </div>
  </q-page>
</template>

<script>

import fs from 'fs'
import path from 'path'

export default {
  name: 'PageIndex',
  data () {
    return {
      sound_play: false,
      sound_mode: 'normal',
      continue_loading: null,
      record_unmask_normal: new Audio('unmask_normal.m4a'),
      record_unmask_kind: new Audio('unmask_kind.m4a'),
      record_unmask_shouting: new Audio('unmask_shouting.m4a'),
      total_detect_number: '載入中...',
      mask_number: '載入中...',
      unmask_number: '載入中...',
    }
  },
  created(){
    
    this.$q.loading.show({
      message: '<span style="font-size:20px; font-weight:bold; font-family:Microsoft JhengHei;">載入中...</span><br/><span style="color:#66ccff; font-size:20px; font-weight:bold; font-family:Microsoft JhengHei;">請稍候片刻</span>'
    })

    this.record_unmask_normal.loop = false
    this.record_unmask_kind.loop = false
    this.record_unmask_shouting.loop = false

    var run = setTimeout(function a(){

      try {
        
        // Do first 
        
        let fileContents = fs.readFileSync(
          path.join(__statics, '../darknet/build/darknet/x64/current.txt'),
          'utf8'
        )

        if (fileContents.length !== 0){
          fileContents = fileContents.slice(0, fileContents.length-3)
          var json_data = JSON.parse(fileContents);
        
          this.total_detect_number = json_data.objects.length

          var temp_mask_number = 0
          var temp_unmask_number = 0


          for(var i = 0; i < json_data.objects.length; i++){
            if (json_data.objects[i].class_id === 0){
              temp_mask_number += 1
            }
            else if (json_data.objects[i].class_id === 1){
              temp_unmask_number += 1
            }
          }

          this.mask_number = temp_mask_number
          this.unmask_number = temp_unmask_number

          // 要是有人沒戴口罩，播放警告音效
          if(this.unmask_number > 0 && this.sound_play === true){
              if(this.sound_mode === 'normal'){
                this.record_unmask_normal.play()
              } 
              else if (this.sound_mode === 'kind'){
                this.record_unmask_kind.play()
              }
              else if (this.sound_mode === 'shouting'){
                this.record_unmask_shouting.play()
              }
          }
        }
                
        // Repeat
        this.continue_loading = setInterval( function readfile(){
          let fileContents = fs.readFileSync(
            path.join(__statics, '../darknet/build/darknet/x64/current.txt'),
            'utf8'
          )

          if (fileContents.length !== 0){
            fileContents = fileContents.slice(0, fileContents.length-3)
            var json_data = JSON.parse(fileContents);

            this.total_detect_number = json_data.objects.length

            var temp_mask_number = 0
            var temp_unmask_number = 0


            for(var i = 0; i < json_data.objects.length; i++){
              if (json_data.objects[i].class_id === 0){
                temp_mask_number += 1
              }
              else if (json_data.objects[i].class_id === 1){
                temp_unmask_number += 1
              }
            }

            // 要是有人沒戴口罩，播放警告音效
            if(this.unmask_number > 0 && this.sound_play === true){
                if(this.sound_mode === 'normal'){
                  this.record_unmask_normal.play()
                } 
                else if (this.sound_mode === 'kind'){
                  this.record_unmask_kind.play()
                }
                else if (this.sound_mode === 'shouting'){
                  this.record_unmask_shouting.play()
                }
            }
            this.mask_number = temp_mask_number
            this.unmask_number = temp_unmask_number
          }
        }.bind(this)
        , 1000)
      } catch(e){
        console.error(e)
      }
      this.$q.loading.hide()
    }.bind(this), 2000)
  },
  mounted(){

  },
  methods: {
    turn_sound_off(){
      this.sound_play = false
    },
    turn_sound_on(){
      this.sound_play = true
    }
  },
  beforeRouteLeave (to, from, next) {
    if(this.continue_loading)
        clearInterval(this.continue_loading);
    next();
  },
}
</script>
