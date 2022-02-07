export interface TweetResponse {
  data: {
    text: string;
    entities: Entities;
    created_at: string;
    public_metrics: PublicMetrics;
    conversation_id: string;
    id: string;
  }[];
}

export interface Entities {
  hashtags?: Hashtag[] | null;
  urls?: TweetUrl[] | null;
}

export interface Hashtag {
  start: number;
  end: number;
  tag: string;
}

export interface TweetUrl {
  start: number;
  end: number;
  url: string;
  expanded_url: string;
  display_url: string;
}

export interface PublicMetrics {
  retweet_count: number;
  reply_count: number;
  like_count: number;
  quote_count: number;
}
