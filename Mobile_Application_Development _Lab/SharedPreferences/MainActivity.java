package com.example.sharedpreferences;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText username, password;
    Button btn;
    SharedPreferences sp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username=findViewById(R.id.uname);
        password=findViewById(R.id.upswrd);
        btn=findViewById(R.id.login_btn);
        sp=getSharedPreferences("Login",MODE_PRIVATE);
    }

    public void onClick(View view) {
        SharedPreferences.Editor ed=sp.edit();
        ed.putString("Username", username.getText().toString());
        ed.putString("Password",password.getText().toString());
        ed.commit();
        Intent i=new Intent(MainActivity.this, MainActivity2.class);
        startActivity(i);
    }
}