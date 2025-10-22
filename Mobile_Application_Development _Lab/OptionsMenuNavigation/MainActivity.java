package com.example.optionsmenunavigation;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu){
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.samplemenu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        int id = item.getItemId();

        if (id == R.id.menu_account) {
            Intent i = new Intent(MainActivity.this, MainActivity2.class);
            startActivity(i);
            Toast.makeText(this, "Account Settings clicked", Toast.LENGTH_SHORT).show();
        }
        else if (id == R.id.menu_notifications) {
            Intent i = new Intent(MainActivity.this, MainActivity3.class);
            startActivity(i);
            Toast.makeText(this, "Notification Settings clicked", Toast.LENGTH_SHORT).show();
        }
        else if (id == R.id.menu_help) {
            Intent i = new Intent(MainActivity.this, MainActivity4.class);
            startActivity(i);
            Toast.makeText(this, "Help & Support clicked", Toast.LENGTH_SHORT).show();
        }

        return super.onOptionsItemSelected(item);
    }
}