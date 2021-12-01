use std::time::Instant;


pub fn main() {
    let now = Instant::now();
    let lean_list_i: Vec<u128> = vec![0, 11, 17, 35, 40, 46, 48, 58, 67];
    let lean_list_val: Vec<u128> = vec![17, 37, 571, 13, 23, 29, 401, 41, 19];
    let mut ts: u128 = 571 * 175131348511 - 17;
    let mut counter: u128 = 99999999999781;
    loop {
        let mut valid = true;
        for (x, y) in lean_list_i.iter().zip(&lean_list_val) {
            if (&ts + x) % y != 0 {
                valid = false;
                ts += 571;
            }
        }
        if valid {
            println!("ts is {}", ts);
            println!("Script took: {} seconds", now.elapsed().as_secs());
            return
        }
        else if ts > counter {
                println!("Current value: {}", ts);
                counter += 99999999999780 / 1000;
            }
        }
    }