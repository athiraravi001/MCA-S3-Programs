package com.example.logintologointerface;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity {

    LinearLayout logoCopilot, logoChatGPT;
    TextView logoDetails;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        logoCopilot = findViewById(R.id.copilotlogo);
        logoChatGPT = findViewById(R.id.chatgptlogo);
        logoDetails = findViewById(R.id.tvDetails);
    }

    public void onClick1(View view) {
        logoDetails.setText("ChatGPT is an advanced AI chatbot that understands questions and responds in a human-like way.");
        //Toast.makeText(MainActivity2.this, "ChatGPT is an advanced AI chatbot created by OpenAI that uses a large language model to understand questions and respond in a human-like way.", Toast.LENGTH_LONG).show();
    }

    public void onClick2(View view) {
        logoDetails.setText("Copilot is an AI-powered virtual assistant that helps improve productivity by giving smart suggestions, automating tasks, and analyzing information.");
        //Toast.makeText(MainActivity2.this, "Copilot is an AI-powered virtual assistant that helps improve productivity by giving smart suggestions, automating tasks, and analyzing information.", Toast.LENGTH_LONG).show();
    }
}