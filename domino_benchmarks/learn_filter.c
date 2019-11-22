//#include "hashes.h"

struct Packet {
  int sport;
  int dport;
  int member;
  int filter1_idx;
  int filter2_idx;
  int filter3_idx;
};

#define NUM_ENTRIES 256

int filter1[NUM_ENTRIES] = {0};
int filter2[NUM_ENTRIES] = {0};
int filter3[NUM_ENTRIES] = {0};

void func(struct Packet pkt) {
//  pkt.filter1_idx = hash2a(pkt.sport, pkt.dport) % NUM_ENTRIES;
//  pkt.filter2_idx = hash2b(pkt.sport, pkt.dport) % NUM_ENTRIES;
//  pkt.filter3_idx = hash2c(pkt.sport, pkt.dport) % NUM_ENTRIES;
//  pkt.filter1_idx = pkt.filter1_idx;  
//  pkt.filter2_idx = pkt.filter2_idx; 
//  pkt.filter3_idx = pkt.filter3_idx;
  if (filter1[pkt.filter1_idx] != 0 &&
      filter2[pkt.filter2_idx] != 0 &&
      filter3[pkt.filter3_idx] != 0)
     pkt.member = 1; 
//  pkt.member = (filter1[pkt.filter1_idx] &&
//                filter2[pkt.filter2_idx] &&
//                filter3[pkt.filter3_idx]);

  filter1[pkt.filter1_idx] = 1;
  filter2[pkt.filter2_idx] = 1;
  filter3[pkt.filter3_idx] = 1;
}
