inputFileName='Chorus.wav';
outputFileName='reversed chorus.wav';
[inputData, sampleRate]= audioread("Chorus.wav");
reversedData=flipud(inputData);
audiowrite(outputFileName, reversedData, sampleRate);
disp('Audio file reversed and saved successfully');
