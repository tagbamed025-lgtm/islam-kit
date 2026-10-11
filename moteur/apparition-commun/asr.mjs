import { pipeline, env } from '@xenova/transformers';
import fs from 'fs';
env.localModelPath='/home/claude/travail/had/asr/package/models/'; env.allowRemoteModels=false;
const asr=await pipeline('automatic-speech-recognition','Xenova/whisper-small',{quantized:true});
for (const id of process.argv.slice(2)){
 const buf=fs.readFileSync(`${id}/voix16.f32`); const audio=new Float32Array(buf.buffer,buf.byteOffset,buf.length/4);
 const out=await asr(audio,{language:'french',task:'transcribe',return_timestamps:'word',chunk_length_s:30,stride_length_s:5});
 fs.writeFileSync(`${id}/align_words.json`,JSON.stringify(out,null,1)); console.log(id,out.text.slice(0,80));
}
