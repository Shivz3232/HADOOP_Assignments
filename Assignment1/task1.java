package hadoop;

import java.io.IOException;
import java.time.LocalDate;

import javax.swing.text.html.HTMLEditorKit.Parser;

import org.json.JSONObject;

import jdk.nashorn.internal.objects.Global;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class task1 extends Configured implements Tool {
    public static class wordRecognizedMapper extends Mapper<Object, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private final static IntWritable zero = new IntWritable(0);
        private Text word1 = new Text();
        private Text word2 = new Text();
        private Text inputString = new Text();

        public void setup(Context context) {
            Configuration config = context.getConfiguration();
            String wordstring = config.get("inputString");
            inputString.set(wordstring);
        }

        public Boolean spc(String word) {
            String specialCharactersString = "!@#$%&*()'+,-./:;<=>?[]^_`{|}";
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                if (specialCharactersString.contains(Character.toString(ch))) {
                    return true;
                } else if (i == word.length() - 1) {
                    return false;
                }
            }
            return true;
        }

        public boolean isStringUpperCase(String str) {
            char[] charArray = str.toCharArray();
            for (int i = 0; i < charArray.length; i++) {
                if (!Character.isUpperCase(charArray[i]))
                    return false;
            }

            return true;
        }

        public Boolean badrecord(JSONObject obj) {
            if (!spc(obj.get("word").toString())) {
                if (obj.get("key_id").toString().length() == 16) {
                    if (obj.get("recognized").toString().equals("true")
                            || obj.get("recognized").toString().equals("false")) {
                        if (obj.get("countrycode").toString().length() == 2) {
                            if (isStringUpperCase(obj.get("countrycode").toString())) {
                                return false;
                            }
                        }
                    }
                }
            }
            return true;
        }

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            JSONObject jsonObject = new JSONObject(value.toString());

            String inputString = context.getConfiguration().get("inputString");

            String temp = jsonObject.get("word").toString();

            if (!badrecord(jsonObject) && temp.equals(inputString.toString())) {
                word1.set("task1a");
                word2.set("task1b");
                if (Boolean.valueOf(jsonObject.get("recognized").toString())) {
                    context.write(word1, one);
                } else {
                    context.write(word1, zero);
                }

                LocalDate day = LocalDate.parse(jsonObject.get("timestamp").toString().substring(0, 10));

                if (day.getDayOfWeek().toString().equals("SUNDAY")
                        || day.getDayOfWeek().toString().equals("SATURDAY")) {
                    if (Boolean.valueOf(jsonObject.get("recognized").toString())) {
                        context.write(word2, zero);
                    } else {
                        context.write(word2, one);
                    }
                }
            }
        }
    }

    public static class didRecognizeReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();
        // private Text lol = new Text();

        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    @Override
    public int run(String[] args) throws Exception {
        String inputString = args[2];

        Configuration conf = new Configuration();
        conf.set("inputString", inputString);

        Job job = Job.getInstance(conf, "Recognized Words");

        job.setJarByClass(task1.class);

        job.setMapperClass(wordRecognizedMapper.class);
        job.setCombinerClass(didRecognizeReducer.class);
        job.setReducerClass(didRecognizeReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        return (job.waitForCompletion(true) ? 0 : 1);
    }

    public static void main(String[] args) throws Exception {
        int res = ToolRunner.run(new Configuration(), new task1(), args);
    }
}