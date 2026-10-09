import { pipeline, env } from '@xenova/transformers';
import fs from 'fs';
env.localModelPath='/home/claude/w/node_modules/sts-whisper-small/models/'; env.allowRemoteModels=false;
const buf=fs.readFileSync(process.argv[2]); const audio=new Float32Array(buf.buffer,buf.byteOffset,buf.length/4);
const asr=await pipeline('automatic-speech-recognition','Xenova/whisper-small',{quantized:true});
const mode=process.argv[3]||'word';
const out=await asr(audio,{language:process.argv[5]||'french',task:'transcribe',return_timestamps: mode==='word'?'word':true,chunk_length_s:30,stride_length_s:5});
fs.writeFileSync(process.argv[4],JSON.stringify(out,null,1)); console.log(out.text);
